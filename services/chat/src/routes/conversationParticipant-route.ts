import { getAllConversationParticipant, getParticipantById, postConversationParticipant, putConversationParticipant, deleteConversationParticipant } from "../controllers/conversationParticipant-controller";
import express from "express";

const router = express.Router();

router.get("/", getAllConversationParticipant);
router.get("/:id", getParticipantById);
router.post("/", postConversationParticipant);
router.put("/:id", putConversationParticipant);
router.delete("/:id", deleteConversationParticipant);

export default router;