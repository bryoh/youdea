'use strict'
var supportsAudio = !! document.createElement('audio').canPlayType;
if (supportsAudio) {
    var player = new Plyr('#audio', { 
        controls: [
            'rewind',
            'play',
            'progress',
            'current-time',
            'duration',
            'fast-forward',
            'download',
        ]
    });
    var currentTrack = 0,
        playing = false,
        npAction = $('#npAction'),
        npTitle = $('#npTitle'),
        audio = $('#audio').on('play', function() {
            playing = true;
            npAction.text('Playing...');
        }).on('pause', function() {
            playing = false;
            npAction.text('Paused...')
        }).on('ended', function() {
            playing = false;
            npAction.text('Paused...')
        }).get(0),
        row = $('.clickable-row').click(function (){
            var fileurl = $(this).attr('data-href');
            audio.src = fileurl; 
            //alert(fileurl);
            player.on('loadedmetadata', function() {
                $('a[data-plyr="download"]').attr('href', fileurl);
            });
            audio.play();
        })


} else {
    // no audio suppport
    var noSupport = 'No support'
}

