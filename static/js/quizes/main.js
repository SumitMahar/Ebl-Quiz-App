const modalBtns = [...document.getElementsByClassName('quiz-modal-button')]
const modalBody = document.getElementById('modal-quiz-detail')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    // custom attributes
    const pk = modalBtn.getAttribute('data-pk')
    const quizName = modalBtn.getAttribute('data-quiz-name')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const duration = modalBtn.getAttribute('data-duration')
    const quizUrl = modalBtn.getAttribute('data-quiz-url')

    // changing body of the modal
    modalBody.innerHTML = `
    <div class="h5 mb-3">
        Are you sure you want to begin "<b>${quizName}"</b>
    </div>
    <div class="text-muted">
        <ul>
            <li>Difficulty: <b>${difficulty}</b></li>
            <li>Number of questions: <b>${numQuestions}</b> </li>
            <li>Score to pass: <b>${scoreToPass}%</b> </li>
            <li>Duration: <b>${duration}</b> </li>
        </ul>
    </div>
    `
    // adding event listener for starting the quiz
    startBtn.addEventListener('click', () => {
        window.location.href = new URL(quizUrl, url).href
    })
}))




