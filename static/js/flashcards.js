function updateProgress(word, correct) {
    fetch('/update_progress', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: word, correct: correct })
    });
}
