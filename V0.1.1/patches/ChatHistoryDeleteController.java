package xiaozhi.modules.agent.controller;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import xiaozhi.common.utils.Result;
import xiaozhi.common.utils.ResultUtils;
import java.util.List;
import java.util.ArrayList;

@RestController
@RequestMapping("/agent/chat-history")
public class ChatHistoryDeleteController {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @DeleteMapping("/delete/{id}")
    public Result<Object> deleteChatHistoryById(@PathVariable Long id) {
        try {
            String audioId = jdbcTemplate.queryForObject(
                "SELECT audio_id FROM ai_agent_chat_history WHERE id = ?",
                String.class, id
            );

            if (audioId != null && !audioId.isEmpty()) {
                jdbcTemplate.update("DELETE FROM ai_agent_chat_audio WHERE id = ?", audioId);
            }

            int deleted = jdbcTemplate.update("DELETE FROM ai_agent_chat_history WHERE id = ?", id);

            if (deleted == 0) {
                return ResultUtils.error("记录不存在");
            }

            return ResultUtils.success("删除成功");
        } catch (Exception e) {
            return ResultUtils.error("删除失败: " + e.getMessage());
        }
    }

    @DeleteMapping("/delete-session/{sessionId}")
    public Result<Object> deleteChatHistoryBySessionId(@PathVariable String sessionId) {
        try {
            List<String> audioIds = jdbcTemplate.queryForList(
                "SELECT audio_id FROM ai_agent_chat_history WHERE session_id = ? AND audio_id IS NOT NULL",
                String.class, sessionId
            );

            for (String audioId : audioIds) {
                if (audioId != null && !audioId.isEmpty()) {
                    jdbcTemplate.update("DELETE FROM ai_agent_chat_audio WHERE id = ?", audioId);
                }
            }

            jdbcTemplate.update("DELETE FROM ai_agent_chat_history WHERE session_id = ?", sessionId);
            jdbcTemplate.update("DELETE FROM ai_agent_chat_title WHERE session_id = ?", sessionId);

            return ResultUtils.success("删除成功");
        } catch (Exception e) {
            return ResultUtils.error("删除失败: " + e.getMessage());
        }
    }
}
