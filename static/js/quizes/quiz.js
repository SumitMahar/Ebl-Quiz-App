var url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('display-result')
const timerBox = document.getElementById('timer-box')

const activateTimer = (time) => {

    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00`
    }
    // 2 = 1:59
    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(() => {
        seconds--
        if (seconds < 0) {
            seconds = 59
            minutes--
        }
        if (minutes.toString().length < 2) {
            displayMinutes = `0${minutes}`
        }
        else {
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2) {
            displaySeconds = `0${seconds}`
        }
        else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = '00:00'
            clearInterval(timer)
            sendData()
        }
        timerBox.innerHTML = `${displayMinutes}:${displaySeconds}`
    }, 1000)

}


$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        console.log(response)
        let data = response.data
        let q_no = 1
        let questionAndAnswers = ''
        data.forEach(element => {
            for (const [question, answers] of Object.entries(element)) {
                questionAndAnswers += `
                <div class="row gy-4 mt-1">
                    <div class="col-md-12">
                        <div class="card bg-white text-dark shadow h-100">
                            <div class="card-body">
                                <h5>${q_no}. ${question}</h5>
                `
                answers.forEach(answer => {
                    questionAndAnswers += `
                            <div>
                                <input type="radio" class="mx-4 ans" id="${question}-${answer}" name="${question}" value="${answer}">
                                <lable for="${question}">${answer}</lable>
                            </div>
                    `
                });
                questionAndAnswers += `
                            </div>
                        </div>
                    </div>
                </div>
                `
            }

            q_no += 1
        });
        quizBox.innerHTML = questionAndAnswers
        activateTimer(response.duration)
    },

    error: function (error) {
        console.log(error)
    }

})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const data = {}
    const elements = [...document.getElementsByClassName('ans')]

    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }

    })
    $.ajax({
        type: 'POST',
        url: `${url}save`,
        data: data,
        success: function (response) {
            // console.log(response)
            quizForm.classList.add('not-visible')

            scoreBox.innerHTML = `${response.passed ? 'Well done you passed!' : 'better luck next time'} Your score is ${response.score}%`

            const results = response.results
            results.forEach(res => {
                const resDiv = document.createElement('div')
                for (const [ques, resp] of Object.entries(res)) {
                    resDiv.innerHTML += ques
                    const cls = ['container', 'p-3', 'text-light', 'h6', 'shadow', 'card', 'card-body']
                    resDiv.classList.add(...cls)

                    if (resp == 'not answered') {
                        resDiv.innerHTML += ' - not answered'
                        resDiv.classList.add('bg-danger')
                    }
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` | answered: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | "correct answer: ${correct}"`
                            resDiv.innerHTML += ` answered: ${answer}`
                        }

                    }

                }
                resultBox.append(resDiv)
            })

        },
        error: function (error) {
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    sendData()
})