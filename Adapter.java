interface OldMediaPlayer {
    void playMp3(String filename);
}

class OldMediaPlayerImpl implements OldMediaPlayer {
    @Override
    public void playMp3(String filename) {
        System.out.println("Tocando arquivo MP3: " + filename);
    }
}

interface MediaPlayer {
    void play(String audioType, String filename);
}

class MediaAdapter implements MediaPlayer {
    private OldMediaPlayer oldMediaPlayer;

    public MediaAdapter() {
        this.oldMediaPlayer = new OldMediaPlayerImpl();
    }

    @Override
    public void play(String audioType, String filename) {
        if (audioType.equalsIgnoreCase("mp3")) {
            oldMediaPlayer.playMp3(filename);
        } else {
            System.out.println("Formato não suportado: " + audioType);
        }
    }
}

class AudioPlayer implements MediaPlayer {
    private MediaAdapter mediaAdapter;

    public AudioPlayer() {
        this.mediaAdapter = new MediaAdapter();
    }

    @Override
    public void play(String audioType, String filename) {
        if (audioType.equalsIgnoreCase("mp3") || audioType.equalsIgnoreCase("mp4")) {
            mediaAdapter.play(audioType, filename);
        } else {
            System.out.println("Formato não suportado: " + audioType);
        }
    }
}

public class AdapterPatternDemo {
    public static void main(String[] args) {
        AudioPlayer audioPlayer = new AudioPlayer();

        audioPlayer.play("mp3", "musica.mp3");
        audioPlayer.play("mp4", "video.mp4");
        audioPlayer.play("wav", "audio.wav");
    }
}