// in src/posts.js
import * as React from "react";
import {
  List,
  Datagrid,
  TextField,
  // ReferenceField,
  EditButton,
  DeleteButton,
  Edit,
  Create,
  SimpleForm,
  ReferenceInput,
  SelectInput,
  TextInput,
  EmailField,
} from "react-admin";

// const postFilters = [
//   <TextInput source="q" label="Search" alwaysOn />,
//   <ReferenceInput source="userId" label="User" reference="users" allowEmpty>
//     <SelectInput optionText="name" />
//   </ReferenceInput>,
// ];

const postFilters = [
  <TextInput source="q" label="Search" alwaysOn />,
  // <ReferenceInput source="userId" label="User" reference="users" allowEmpty>
  <ReferenceInput source="id" label="User" reference="users" allowEmpty>
    <SelectInput optionText="name" />
  </ReferenceInput>,
  <ReferenceInput source="email" label="email" reference="users" allowEmpty>
    <SelectInput optionText="email" />
  </ReferenceInput>,
];

export const UserList = (props) => (
  <List filters={postFilters} {...props}>
    {/* <List {...props}> */}
    <Datagrid>
      <TextField source="id" />
      <TextField source="name" />
      {/* <ReferenceField source="userId" reference="users">
        <TextField source="name" />
      </ReferenceField> */}
      <EmailField source="email" />
      <EditButton basePath="/users" />
      <DeleteButton basePath="/users" />
    </Datagrid>
  </List>
);

// const UserTitle = ({ record }) => {
//   return <span>Post {record ? `"${record.title}"` : ""}</span>;
// };

export const UserEdit = (props) => (
  //   <Edit title={<UserTitle />} {...props}>
  <Edit title="Edit user" {...props}>
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput source="name" />
      <TextInput source="email" />
    </SimpleForm>
  </Edit>
);

export const UserCreate = (props) => (
  <Create {...props}>
    <SimpleForm>
      {/* <ReferenceInput source="userId" reference="users">
        <SelectInput optionText="name" />
      </ReferenceInput> */}
      <TextInput source="id" />
      <TextInput source="name" />
      <TextInput source="email" />
    </SimpleForm>
  </Create>
);
