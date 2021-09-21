rootURL = "http://127.0.0.1:5000"
window.addEventListener("load", init);

function init() {  // equivalent to main method
    const signIn = document.getElementById('signIn')
    signIn.addEventListener('click', toSignIn)

    const signUp = document.getElementById('signUp')
    signUp.addEventListener('click', toSignUp)

    const shot = document.getElementById('shot')
    shot.addEventListener('click', toShot)

    camera()
}

function toSignIn() {
    console.log("hey")
    fetch(rootURL + "/signin")
        .then(statusCheck)
        .then(resp => resp.text())
        .then((responseData) => alert(responseData))
        .catch(() => alert("Error occurred"))
}

async function statusCheck(response) {
    if (!response.ok) {
        console.log("status check not ok")
        throw new Error(await response.text())
    }
    console.log("status check ok")
    return response
}

function toSignUp() {
    fetch(rootURL + "/signup")
        .then(statusCheck)
        .then(resp => resp.text())
        .then((responseData) => alert(responseData))
        .catch(() => alert("Error occurred"))
}

function toShot() {
    const canvas = document.querySelector('canvas')
    const video = document.querySelector('video')

    video.pause()

    const param = new FormData()
    param.append('image', canvas.toDataURL())
    fetch(rootURL + "/shot", {
        method : "POST",
        body : param
    }).then()
        .catch(() => alert("Error occurred"))
}

/**
 * Open webcam
 */
function camera() {
    /*let stream = null   // primitive version
    try {
        stream = await navigator.mediaDevices.getUserMedia(constraints)
        const video = document.querySelector('video')
        video.srcObject = stream
    } catch (err) {
        alert('Failed to take photo. Please enable your webcam.')
    }*/
    navigator.mediaDevices.getUserMedia({
        audio: false,
        video: {
            width: {min: 50},
            height: {min: 50}
        }
    }).then(getStream)
        .catch(() => {
            alert('Failed to take photo. Please enable your webcam.')
        })
}

/**
 * Let canvas and video camera work together
 * @param stream
 */
function getStream(stream) {
    const video = document.querySelector('video')
    const canvas = document.querySelector('canvas')
    const ctx = canvas.getContext("2d")

    video.srcObject = stream

    canvasInterval = window.setInterval(() => {
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
    }, 1000 / 30)

    video.onplay = function() {
        clearInterval(canvasInterval);
        canvasInterval = window.setInterval(() => {
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
            ctx.strokeStyle = 'red'
            ctx.strokeRect(120, 50, 160, 200)
        }, 1000 / 30);
    };

    video.onended = function () {
        clearInterval(canvasInterval)
    }
}
