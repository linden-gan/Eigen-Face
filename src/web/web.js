const signIn = document.getElementById('signIn')
signIn.addEventListener('click', toSignIn)

const signUp = document.getElementById('signUp')
signUp.addEventListener('click', toSignUp)

const constraint = {
    audio: false,
    video: {
        width: { min: 60 },
        height: { min: 100 }
    }
}

function toSignIn() {
    document.body.style.backgroundColor = 'rgb(100, 200, 100)'
    let stream = shot({
    audio: false,
    video: {
        width: { min: 60 },
        height: { min: 100 }
    }})
    stream.catch()
}

function toSignUp() {

}

async function shot(constraints) {
    let stream = null
    try {
        stream = await navigator.mediaDevices.getUserMedia(constraints)
    } catch (err) {
        alert('Failed to take photo. Please enable your webcam.')
    }
    return stream
}