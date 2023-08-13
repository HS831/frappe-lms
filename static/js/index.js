const issueForm = document.querySelector('.issue--form')
const returnForm = document.querySelector('.return_book--form')
const memberForm = document.querySelector('.add_member--form')

const issue = async (data ) => {
    const URL = window.location
    try {
        const response = await fetch(`${URL.protocol}//${URL.host}/api/books/issueBook`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();

        if (responseData.issue_id) {
            alert('Book issued!');
            window.setTimeout(() => {
                location.assign('/books');
            }, 1500);
        }
    } catch (err) {
        console.log(err)
    }
}

const take_return = async (data) => {
    const URL = window.location
    try {
        const response = await fetch(`${URL.protocol}//${URL.host}/api/books/issueReturn`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();

        if (responseData) {
            alert('Book returned!');
            window.setTimeout(() => {
                location.assign('/books');
            }, 1500);
        }
    } catch (err) {
        console.log(err)
    }
}

const add_member = async (data) => {
    const URL = window.location

    try {
        const response = await fetch(`${URL.protocol}//${URL.host}/api/members`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();

        if (responseData) {
            alert('Member Added!');
            window.setTimeout(() => {
                location.assign('/books');
            }, 1500);
        }
    } catch (err) {
        console.log(err)
    }
}


if(issueForm) {
    issueForm.addEventListener('submit', (e) => {
        e.preventDefault()
        const issue_id = document.getElementById('issue_id').value
        const book_id = document.getElementById('book_id').value
        const member_id = document.getElementById('member_id').value
        const issue_date = document.getElementById('issue_date').value

        let data = {
            issue_id,
            book_id,
            member_id,
            issue_date
        }
        issue(data);
    })
}

if(returnForm) {
    returnForm.addEventListener('submit', e => {
        e.preventDefault()
        const issue_id = document.getElementById('issue_id').value
        const return_date = document.getElementById('return_date').value
       
        let data = {
            issue_id,
            return_date
        }
    
        take_return(data)
    })
}

if(memberForm) {
    memberForm.addEventListener('submit', (e) => {
        e.preventDefault()
        const member_id = document.getElementById('member_id').value
        const name = document.getElementById('name').value
        const email = document.getElementById('email_id').value
        
        let data = {
            member_id,
            name,
            email
        }

        add_member(data)
    })
}