const form = document.getElementById('register-form');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const birthdateInput = document.getElementById('birthdate');
const genderInput = document.getElementById('gender');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    // Reset error messages
    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(message => message.textContent = '');

    // Validate form inputs
    let isValid = true;

    if (!validateUsername(usernameInput.value)) {
        document.getElementById('username-error').textContent = 'Please enter a valid username.';
        isValid = false;
    }

    if (!validateEmail(emailInput.value)) {
        document.getElementById('email-error').textContent = 'Please enter a valid email address.';
        isValid = false;
    }

    if (!validatePassword(passwordInput.value)) {
        document.getElementById('password-error').textContent = 'Password must be at least 8 characters long and contain a mix of uppercase and lowercase letters, numbers, and symbols.';
        isValid = false;
    }

    if (confirmPasswordInput.value !== passwordInput.value) {
        document.getElementById('confirm-password-error').textContent = 'Passwords do not match.';
        isValid = false;
    }

    if (!validateBirthdate(birthdateInput.value)) {
        document.getElementById('birthdate-error').textContent = 'Please enter a valid birthdate.';
        isValid = false;
    }

    if (!validateGender(genderInput.value)) {
        document.getElementById('gender-error').textContent = 'Please select a gender.';
        isValid = false;
    }

    if (isValid) {
        // Submit form
        alert('Registration successful!');
        form.reset();
    }
});

function validateUsername(username) {
    const usernameRegex = /^[a-zA-Z0-9_]{5,20}$/;
    return usernameRegex.test(username);
}

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
    return emailRegex.test(email);
}

function validatePassword(password) {
    const passwordRegex = /^(?=.\d)(?=.[a-z])(?=.[A-Z])(?=.[!@#$%^&*()_+-=[]{};':"\|,.<>/ ? ]). {
    8,
}
$ / ;
return passwordRegex.test(password);
}

function validateBirthdate(birthdate) {
    const birthdateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!birthdateRegex.test(birthdate)) {
        return false;
    }

    const today = new Date();
    const birthdateDate = new Date(birthdate);
    const age = today.getFullYear() - birthdateDate.getFullYear();
    const monthDiff = today.getMonth() - birthdateDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthdateDate.getDate())) {
        age--;
    }

    return age >= 18;
}

function validateGender(gender) {
    return gender !== '';
}