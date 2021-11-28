import React from "react";
import { Admin, Resource } from "react-admin";
// import restProvider from "ra-data-simple-rest";
// import simpleRestProvider from "ra-data-simple-rest";
import { UserList, UserEdit, UserCreate } from "./components/Users";
import dataProvider from "./dataProvider";
import Dashboard from "./components/Dashboard";

// import UserList from "./component/UserList";
// import UserCreate from "./component/UserCreate";
// import UserEdit from "./component/UserEdit";
// import UserIcon from "@material-ui/icons/Group";
// import dataProvider from "./dataProvider";

const App = () => {
  return (
    //<Admin dataProvider={restProvider("http://localhost:5000")}>
    <Admin dashboard={Dashboard} dataProvider={dataProvider}>
      <Resource
        name="users"
        list={UserList}
        create={UserCreate}
        edit={UserEdit}
        // icon={UserIcon}
      />
    </Admin>
  );
};

export default App;
