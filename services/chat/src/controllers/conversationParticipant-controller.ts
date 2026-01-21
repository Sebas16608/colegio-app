import ConversationParticipant from "models/conversationParticipant";
import { Request, Response } from "express";

const getAllConversationParticipant = async (req: Request, res: Response) => {
       try {
            const participant = await ConversationParticipant.findAll()
            res.status(200).json(participant);
    } catch (error) {
            res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}