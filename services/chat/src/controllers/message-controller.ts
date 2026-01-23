import Message from "models/message";
import { Request, Response } from "express";

const getAllMessages = async (req: Request, res: Response) => {
    try {
        const message = await Message.findAll();
        return res.status(200).json(message)
    } catch (error) {
        return res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}

const getMessagesById = async (req: Request, res: Response) => {
    try {
        const id = Number(req.params);
        const message = await Message.findByPk(id);
        
        if (!message) return res.status(404).json({ error: "Not Found"});

        res.status(200).json(message);
    } catch (error) {
        return res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}

const postMessage = async (req: Request, res: Response) => {
    try{
        const { conversation_id, content, message_type, is_read} = req.body;
        const message = await Message.create({ conversation_id, content, message_type, is_read });

        return res.status(201).json(message);
    } catch (error) {
        return res.status(400).json({ error: `Bad Request ${error}` });
    }
}

const putMessage = async (req: Request, res: Response) => {
    try {
        const id = Number(req.params);
        const message = await Message.findByPk(id);

        if (!message) return res.status(404).json({ error: "Not Found" });

        const { conversation_id, content, message_type, is_read } = req.body;
        await message.save()
        return res.json(message);
    } catch (error) {
        return res.status(400).json({ error: ` Bad Request ${error}`});
    }
}

const deleteMessage = async (req: Request, res: Response) => {
    try {
        const id = Number(req.params);
        const message = await Message.findByPk(id);

        if (!message) return res.status(404).json({ error: "Not Found" });

        await message.destroy()
        return res.status(204).json({ error: "No Content" });
    } catch (error) {
        return res.status(500).json({ error: `Internal Server Error ${error}`});
    }
}

export default { getAllMessages, getMessagesById, postMessage, putMessage, deleteMessage };
