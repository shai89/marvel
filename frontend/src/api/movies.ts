import axios from "axios";
import { MoviePerActor, ActorsWithMultipleCharacters, CharactersWithMultipleActors, ApiResponse  } from "../types/models";
import { API_BASE_URL } from "../constants/api";

export const fetchMoviesPerActor = async (page: number): Promise<ApiResponse> => {
  const { data } = await axios.get<ApiResponse>(`${API_BASE_URL}/movies-per-actor?page=${page}`);
  return data;
};

export const getMoviesPerActor = async (): Promise<MoviePerActor[]> => {
  const response = await axios.get(`${API_BASE_URL}/movies-per-actor`);
  return response.data;
};

export const getActorsWithMultipleCharacters = async (): Promise<ActorsWithMultipleCharacters> => {
  const response = await axios.get(`${API_BASE_URL}/actors-with-multiple-characters`);
  return response.data;
};

export const getCharactersWithMultipleActors = async (): Promise<CharactersWithMultipleActors> => {
  const response = await axios.get(`${API_BASE_URL}/characters-with-multiple-actors`);
  return response.data;
};