window.addEventListener('DOMContentLoaded', function() {
  var video = document.getElementById('my-video');
  video.addEventListener('play', function() {
    // Действия, выполняемые при воспроизведении видео
    console.log('Видео начало воспроизводиться');
  });

  video.addEventListener('pause', function() {
    // Действия, выполняемые при остановке видео
    console.log('Видео было остановлено');
  });

  video.addEventListener('ended', function() {
    // Действия, выполняемые после завершения видео
    console.log('Видео завершилось');
  });
});
