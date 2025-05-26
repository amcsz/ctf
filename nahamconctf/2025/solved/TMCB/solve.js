(function checkAll() {
    const BATCH_SIZE = 100000; // Avoid overwhelming server
    let index = 0;

    function sendBatch() {

        const batch = [];
        for (let i = 0; i < BATCH_SIZE && index < 2_000_000; i++, index++) {
            if (!checkedBoxes.has(index)) {
                batch.push(index);
                checkedBoxes.add(index); // update local set for UI
            }
        }

        if (batch.length > 0) {
            ws.send(JSON.stringify({ action: "check", numbers: batch }));
            document.getElementById('checked-count').textContent = checkedBoxes.size.toLocaleString();
            setTimeout(sendBatch, 50); // delay between batches
        } else {
            console.log("All checkboxes sent.");
        }
    }

    sendBatch();
})();