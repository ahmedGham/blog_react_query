import useAxios from "../auth/useAxios";
import { useQuery } from "react-query";

const useGetGroupsUserIn = ({id,options}) => {
  const axios = useAxios();


  const getGroupsUserIn = () => {
    return axios({ url: `api/members/${id}/groups` });
  };

  const request = useQuery(["members", id, "groups"], getGroupsUserIn, options);
  return request;
};

export default useGetGroupsUserIn;
