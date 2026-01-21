import app from "./app";
import sequelize from "config/database";

// Importacion de modelos
import Conversations from "models/conversation";
import ConversationParticipant from "models/conversationParticipant";
import Message from "models/message";

const port: number = 3000;

(async () => {
    try {
        await sequelize.authenticate();
        await sequelize.sync();

        console.log("DB sincronizada");

        app.listen(port, () => {
            console.log(`Servidor corriendo en http://localhost:${port}`);
        });
    } catch (error){
        console.log(`Error al iniciar el servidor ${error}`);
    };
});
