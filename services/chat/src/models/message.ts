import { DataTypes, Model } from "sequelize";
import sequelize from "config/database";

class Message extends Model{
    declare id?: number;
    declare conversation_id: number;
    declare sender_id: number;
    declare content: string;
    declare message_type: string;
    declare is_read: boolean;
};


