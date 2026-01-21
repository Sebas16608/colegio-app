import { DataTypes, Model } from "sequelize";
import sequelize from "config/database";

class ConversationParticipant extends Model{
    declare id?: number;
    declare conversation_id: number;
    declare user_id: number;
}

ConversationParticipant.init({
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
            key: "id"
        },
        onDelete: "CASCADE",
        onUpdate: "CASCADE",
    },
    user_id: {
        type: DataTypes.INTEGER,
        allowNull: false,
    }
},{
    sequelize,
    modelName: "Conversation_Participant",
    freezeTableName: true,
    timestamps: true,
    underscored: true
}
);

export default ConversationParticipant;