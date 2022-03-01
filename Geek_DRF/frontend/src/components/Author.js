import React from 'react';


const AuthorItem = ({ author }) => {
    return (
        <tr>

            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
            <td>
                {author.email}
            </td>
        </tr>
    )
}

const AuthorList = ({ authors }) => {
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
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}


export default AuthorList;