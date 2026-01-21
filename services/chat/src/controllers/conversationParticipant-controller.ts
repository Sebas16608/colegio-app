import ConversationParticipant from "models/conversationParticipant";
import { Request, Response } from "express";

const getAllConversationParticipant = async (req: Request, res: Response) => {
    try {
            const participant = await ConversationParticipant.findAll();
            res.status(200).json(participant);
    } catch (error) {
            res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}

const getParticipantById = async (req: Request, res: Response) => {
    try {
        const id = Number(req.params);
        const participant = await ConversationParticipant.findByPk(id)
        
        if (!participant)  return res.status(404).json({ error: "Not Found" });
        
        res.status(200).json(participant);
    } catch (error) {
        res.status(500).json({ error: "Internal Server Error" });
    }
}