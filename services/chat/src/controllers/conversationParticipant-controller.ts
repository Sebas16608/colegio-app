import ConversationParticipant from "../models/conversationParticipant";
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

const postConversationParticipant = async (req: Request, res: Response) => {
    try {
        const { conversation_id, user_id } = req.body;

        const participant = await ConversationParticipant.create({ conversation_id, user_id });
        return res.status(201).json(participant);
    } catch (err) {
        return res.status(400).json({ error: "Bad Request" });
    }
}

const putConversationParticipant = async (req: Request, res: Response) => {
    try {
        const id = Number(req.params);
        const participant = await ConversationParticipant.findByPk(id);
        if (!participant) return res.status(404).json({ error: "Not found" });

        const { conversation_id, user_id } = req.body;
        participant.conversation_id = conversation_id ?? participant.conversation_id;
        participant.user_id = user_id ?? user_id;

        await participant.save();
        return res.json(participant);
    } catch (error) {
       return res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}

const deleteConversationParticipant = async (req: Request, res: Response) => {
    try{
        const id = Number(req.params);
        const participant = await ConversationParticipant.findByPk(id);
        
        if (!participant) return res.status(404).json({ error: "Not Found" });

        await participant.destroy();
        return res.status(204).json({ error: "No Content" });
    } catch (error) {
        return res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}

export { getAllConversationParticipant, getParticipantById, postConversationParticipant, putConversationParticipant, deleteConversationParticipant};