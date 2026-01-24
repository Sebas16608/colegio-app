import express, { Express, Request, Response } from "express";
import morgan from "morgan";
import cors from "cors";

const app = express();

// MIDDLEWARE
app.use(morgan("dev"));
app.use(cors());
app.use(express.json());

// Ruta principal
app.get("/", (req: Request, res: Response) => {
    res.json({
        mensaje: "Bienvenido al apartado de chat",
        endpoints: {
            conversations: "/conversation",
            conversationParticipant: "/conversation-participants",
            message: "/message",
        }
    });
});

// Endpoints
import conversationRouter from "./routes/conversation-route";
import participantRouter from "./routes/conversationParticipant-route";
import messageRouter from "./routes/message-route";

app.use("/conversation", conversationRouter);
app.use("/conversation-participants", participantRouter);
app.use("/message", messageRouter);


export default app;