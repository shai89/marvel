import { FC } from "react";
import { ActorRole } from "../types/actorTypes";

interface Props {
  actorName: string;
  roles: ActorRole[];
}

const ActorRoleCard: FC<Props> = ({ actorName, roles }) => {
  return (
    <div className="bg-white border border-gray-200 rounded-lg shadow p-4 hover:shadow-md transition">
      <h2 className="text-lg font-bold text-indigo-700 mb-3">{actorName}</h2>
      <ul className="space-y-1 text-gray-800">
        {roles.map((role, idx) => (
          <li key={idx} className="text-sm">
            <span className="font-medium text-blue-700">{role.characterName}</span>{" "}
            <span className="text-gray-500 italic">in</span>{" "}
            <span className="italic text-gray-600">{role.movieName}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActorRoleCard;
