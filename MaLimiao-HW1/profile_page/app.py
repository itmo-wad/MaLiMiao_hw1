from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Basic route serving static HTML
@app.route('/')
def home():
    # Redirect to profile page
    return redirect(url_for('profile'))

# Advanced route using template rendering
@app.route('/profile')
def profile():
    # Profile data to pass to template
    profile_data = {
        'name': 'Ma Limiao',
        'title': 'Personal Profile',
        'bio': 'I am currently a student and have been engaged in children‘s programming education, cultivating children’s logical thinking and innovation ability. I am currently studying information security at ITMO University and am committed to exploring innovative solutions in the field of information security.',
        'skills': ['Python', 'Java', 'C++', 'Security', 'deep learning'],
        'profile_image': url_for('static', filename='images/profile.jpg')
    }
    return render_template('profile.html', profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True)