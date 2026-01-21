import { DataTypes, Model } from "sequelize";
import sequelize from "config/database";

class Message extends Model{
    declare id?: number;
    declare conversation_id: number;
    declare content: string;
    declare message_type: string;
    declare is_read: boolean;
};

Message.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true
    },
    conversation_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
        references: {
            model: "Conversation",
            key: "id",
        },
        onDelete: "CASCADE",
        onUpdate: "CASCADE",
    },
    content: {
        type: DataTypes.TEXT,
        allowNull: false
    },
    message_type: {
        type: DataTypes.STRING,
        allowNull: false,
        defaultValue: "Text"
    },
    is_read: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
        defaultValue: false,
    },
},
{
    sequelize,
    modelName: "Message",
    freezeTableName: true,
    underscored: true
}
);

export default Message;