import { Navigate, Outlet } from "react-router-dom";
import useAuth from "../hooks/useAuth";

const AdminOnly = () => {
  const { authState } = useAuth();

  console.log(authState);
  
  return authState?.role === "admin" || authState?.role === "superAdmin" ? (
    <Outlet />
  ) : (
    <Navigate to="/" />
  );
};

export default AdminOnly;
