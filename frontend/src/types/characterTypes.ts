export type CharacterAppearanceType = {
  actorName: string;
  movieName: string;
};

export type CharactersWithMultipleActorsResponse = {
  [characterName: string]: CharacterAppearanceType[];
};
