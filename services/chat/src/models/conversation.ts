import { DataTypes, Model } from "sequelize";
import sequelize from "config/database";

class Conversations extends Model{
    declare id?: number;
    declare type: string;
}

Conversations.init({
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true
    },
    type: {
        type: DataTypes.STRING,
        allowNull: false,
    },
},
{
    sequelize,
    modelName: "Conversation",
    freezeTableName: true,
    underscored: true
}
);

export default Conversations;