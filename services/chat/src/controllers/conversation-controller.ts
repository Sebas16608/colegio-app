import Conversations from "models/conversation";
import { Request, Response } from "express";

const getAllConversations = async (req: Request, res: Response) => {
    try {
        const conversation = await Conversations.findAll();
        res.status(200).json(conversation);
    } catch (err) {
        res.status(500).json({ error: err });
    };
};

const getConversationById = async (req: Request, res: Response) => {
    try {
        const id = Number(req.params);
        
        const conversation = await Conversations.findByPk(id);
        
        if (!conversation) {
            return res.status(404).json({ 
                message: 'Conversación no encontrada' 
            });
        }
        
        return res.status(200).json(conversation);
        
    } catch (error) {
        console.error(error);
        return res.status(500).json({ 
            message: `Error del servidor ${error}` 
        });
    };
};

const postConversation = async (req: Request, res: Response) => {
    try {
        const { type } = req.body;
        const conversation = await Conversations.create({ type });
        return res.status(201).json(conversation);
    } catch (err) {
        res.status(400).json({ error: `Bad Request ${err}`})
    }
}