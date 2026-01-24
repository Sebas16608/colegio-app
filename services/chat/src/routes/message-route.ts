import { getAllMessages, getMessagesById, postMessage, putMessage, deleteMessage } from "../controllers/message-controller";
import express from "express";

const router = express.Router();

router.get("/" ,getAllMessages);
router.get("/:id", getMessagesById);
router.post("/", postMessage);
router.put("/:id", putMessage);
router.delete("/:id", deleteMessage);

export default router;