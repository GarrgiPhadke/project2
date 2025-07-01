from django.shortcuts import render
from contact.models import Contact
from django.core.validators import ValidationError

def contact(request):
    if request.method == 'POST':
        # Collect data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location', 'No location')  # Use default if not provided
        message = request.POST.get('message', 'No message')  # Use default if not provided

        # Validate inputs
        errors = []
        if not name:
            errors.append('Name is required.')
        if not email:
            errors.append('Email is required.')
        if not phone:
            errors.append('Phone number is required.')

        # Validate email and phone formats
        from django.core.validators import EmailValidator, RegexValidator
        
        email_validator = EmailValidator()
        phone_validator = RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."
        )

        try:
            email_validator(email)
        except ValidationError as e:
            errors.append(f"Invalid email format: {e.message}")

        try:
            phone_validator(phone)
        except ValidationError as e:
            errors.append(f"Invalid phone format: {e.message}")

        if errors:
            # If there are errors, render the form again with error messages
            return render(request, 'contact.html', {'errors': errors})

        # If no errors, save to the database
        ins = Contact(name=name, email=email, phone=phone, location=location, message=message)
        ins.save()
        print("The data has been saved to the database.")
        # Optionally, you can redirect to a success page or clear the form
        return render(request, 'contact.html', {'success': True})

    # Handle GET request or initial form rendering
    return render(request, 'contact.html')
