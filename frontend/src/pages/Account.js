import React from "react";
import { useRecoilState } from "recoil";
import { showAPIResponse } from "../api/helpers";
import { updateProfile } from "../api/profile";
import { getImageUrl } from "../helpers/imagesHelper";
import { profileAtom } from "../states/user";
import "./Account.css";

const Account = () => {
  const [profile, setProfile] = useRecoilState(profileAtom);

  const handleUpdate = async () => {
    // turn thumbnail into Data URI and update
    const response = await updateProfile(profile);
    showAPIResponse(response);
  };

  const getNewThumbnail = async (image) => {
    // turn the file into a Data URI string and return it
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (event) => {
        resolve(event.target.result);
      };
      reader.onerror = (error) => {
        reject(error);
      };
      reader.readAsDataURL(image);
    });
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen mb-24">
      <h1 className="text-2xl font-bold mb-5">Minha conta</h1>
      <div className="flex flex-col items-center justify-center space-y-5">
        <div className="flex flex-col items-start justify-start space-y-2">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            value={profile?.username}
            onChange={(e) =>
              setProfile({ ...profile, username: e.target.value })
            }
          />
        </div>
        <div className="flex flex-col items-start justify-start space-y-2">
          <label htmlFor="name">Nome</label>
          <input
            type="text"
            value={profile?.name}
            onChange={(e) => setProfile({ ...profile, name: e.target.value })}
          />
        </div>
        <div className="flex flex-col items-start justify-start space-y-2">
          <label htmlFor="bio">Bio</label>
          <input
            type="text"
            value={profile?.bio}
            onChange={(e) => setProfile({ ...profile, bio: e.target.value })}
          />
        </div>
        <div className="flex flex-col items-start justify-start space-y-2">
          <label htmlFor="location">Localização</label>
          <input
            type="text"
            value={profile?.location}
            onChange={(e) =>
              setProfile({ ...profile, location: e.target.value })
            }
          />
        </div>
        <div className="flex flex-col items-start justify-start space-y-2">
          <label htmlFor="birth_date">Data de nascimento</label>
          <input
            type="date"
            value={profile?.birth_date}
            onChange={(e) =>
              setProfile({ ...profile, birth_date: e.target.value })
            }
          />
        </div>
        {profile?.thumbnail && (
          <div className="flex flex-col items-start justify-start space-y-2">
            <img
              src={getImageUrl(profile?.thumbnail)}
              alt="Thumbnail"
              className="w-20 h-20 rounded-full"
            />
          </div>
        )}
        <div className="flex flex-col items-start justify-start space-y-2">
          <label htmlFor="thumbnail">Imagem de perfil</label>
          <input
            type="file"
            accept="image/*"
            onChange={async (e) => {
              const thumbnailURI = await getNewThumbnail(e.target.files[0]);
              setProfile({
                ...profile,
                thumbnail: thumbnailURI,
              });
            }}
          />
        </div>
        {/* create a update button */}
        <button className="bg-green-700" onClick={() => handleUpdate()}>
          Atualizar
        </button>
      </div>
    </div>
  );
};

export default Account;
