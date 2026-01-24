import { getAllConversations, getConversationById, postConversation, putConversation, deleteConversation} from "../controllers/conversation-controller";
import express from "express";

const router = express.Router();

router.get("/", getAllConversations);
router.get("/:id", getConversationById);
router.post("/", postConversation);
router.put("/:id", putConversation);
router.delete("/:id", deleteConversation);

export default router;