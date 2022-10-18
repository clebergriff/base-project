import { setRecoil } from "recoil-nexus";
import { profileAtom } from "../states/user";
import { getUser } from "./profile";

export const showAPIResponse = (response) => {
  alert(JSON.stringify(response));
};

export const checkUserProfileByToken = async () => {
  const resp = await getUser();
  if (!!resp.error) showAPIResponse(resp.error);
  else setRecoil(profileAtom, resp.data);
};
