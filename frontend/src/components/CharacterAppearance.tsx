import { FC } from "react";
import { CharacterAppearanceType } from "../types/characterTypes";

const CharacterAppearance: FC<CharacterAppearanceType> = ({ actorName, movieName }) => {
  return (
    <li className="flex items-center gap-2 text-gray-700 text-sm">
      <span className="font-medium text-blue-700">{actorName}</span>
      <span className="text-gray-400">as</span>
      <span className="italic flex items-center gap-1 text-gray-600">
        {movieName}
      </span>
    </li>
  );
};

export default CharacterAppearance;
