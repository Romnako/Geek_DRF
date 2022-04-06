import React from 'react';
import Link from 'react-router-dom'


const AuthorItem = ({ item }) => {
    return (
        <tr>

            <td>
                {item.first_name}
            </td>
            <td>
                {item.last_name}
            </td>
            <td>
                {item.birthday_year}
            </td>
            <td>
                {item.email}
            </td>
        </tr>
    )
}

const AuthorList = ({ items }) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            <th>
                Email
            </th>
            {items.map((item) => <AuthorItem item={item} />)}
        </table>
    )
}


export default AuthorList;