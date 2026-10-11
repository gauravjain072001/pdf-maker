const form = document.getElementById('pdfForm');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const payload = {
    title: document.getElementById('title').value,
    author: document.getElementById('author').value,
    content: document.getElementById('content').value,
  };

  const response = await fetch('/api/generate-pdf', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'generated-report.pdf';
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
});
