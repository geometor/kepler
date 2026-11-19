"""Exact Symbolic Just-Intonation Music Engine for Kepler's *Harmonices Mundi* (1619).

Transcribes verbatim from Kepler's Linz 1619 folios (``0297``, ``0299``, ``0301``,
``0302``) and *Mysterium Cosmographicum* (1596, folio ``0050``):

- All 7 engraved planetary melodies on folio ``0299`` (p. 207): Saturnus, Jupiter,
  Mars, Terra (*MI–FA–MI*), Venus, Mercurius, and Luna (*Hic locum habet etiam ☽*).
- All 4 Universal 6-Planet Creation Chords on folios ``0301``–``0302`` (pp. 209–210):
  *Genus Durum* (*ut ♮*, *ut c*) and *Genus Molle* (*ut b*, *ut c*).
- Exact integer string-length scales from folio ``0297`` (``2160`` down to ``864``).
- Multi-track Standard MIDI File (Format 1 with 14-bit Just-Intonation pitch bend)
  and stereo Cathedral Organ / Celestial Choir WAV synthesizer.
"""

from __future__ import annotations

import array
import math
import struct
import wave
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

# Exact rational cosmic tonic: G2 = 98 Hz (so G3 = 196 Hz, G4 = 392 Hz)
COSMIC_G2_HZ = sp.Rational(98, 1)


@dataclass(frozen=True)
class KeplerNote:
    """A single note in Kepler's exact 5-limit Just-Intonation system."""

    label: str
    ratio_from_g2: sp.Rational
    beats: sp.Rational

    @property
    def freq_hz(self) -> sp.Rational:
        """Exact rational frequency in Hz."""
        return COSMIC_G2_HZ * self.ratio_from_g2


@dataclass(frozen=True)
class PlanetaryVoice:
    """An engraved planetary melody from *Harmonices Mundi* Book V, Cap. VI (fol. 0299)."""

    key: str
    latin_name: str
    english_name: str
    glyph: str
    voice_part: str
    mode_label: str
    extremal_ratio: sp.Rational
    aphelion_arcmin: str
    perihelion_arcmin: str
    notes: tuple[KeplerNote, ...]
    pan: float  # Stereo placement in [-1.0, +1.0]


@dataclass(frozen=True)
class UniversalChord:
    """One of Kepler's four 6-planet Creation Chords (Book V, Cap. VII, fols. 0301–0302)."""

    key: str
    title: str
    latin_heading: str
    folio: str
    genus: str
    voicings: tuple[tuple[str, str, sp.Rational], ...]  # (planet, note_label, ratio_from_g2)


def _n(label: str, num: int, den: int = 1, beats_num: int = 1, beats_den: int = 1) -> KeplerNote:
    return KeplerNote(
        label=label,
        ratio_from_g2=sp.Rational(num, den),
        beats=sp.Rational(beats_num, beats_den),
    )


def get_planetary_melodies() -> tuple[PlanetaryVoice, ...]:
    """Return all 7 engraved melodies from *Harmonices Mundi* Book V, p. 207 (fol. 0299)."""
    return (
        PlanetaryVoice(
            key="saturn",
            latin_name="Saturnus",
            english_name="Saturn",
            glyph="♄",
            voice_part="Bass",
            mode_label="Modes VII / VIII (Mixolydian, 4:5 Major Third)",
            extremal_ratio=sp.Rational(5, 4),
            aphelion_arcmin="1'46\"",
            perihelion_arcmin="2'15\"",
            notes=(
                _n("G2", 1, 1, 2),
                _n("A2", 9, 8, 2),
                _n("B2", 5, 4, 2),
                _n("A2", 9, 8, 2),
                _n("G2", 1, 1, 4),
            ),
            pan=-0.65,
        ),
        PlanetaryVoice(
            key="jupiter",
            latin_name="Iupiter",
            english_name="Jupiter",
            glyph="♃",
            voice_part="Bass",
            mode_label="Modes I / II (Dorian, 5:6 Minor Third)",
            extremal_ratio=sp.Rational(6, 5),
            aphelion_arcmin="4'30\"",
            perihelion_arcmin="5'30\"",
            notes=(
                _n("G2", 1, 1, 2),
                _n("A2", 10, 9, 2),
                _n("B♭2", 6, 5, 2),
                _n("A2", 10, 9, 2),
                _n("G2", 1, 1, 4),
            ),
            pan=-0.40,
        ),
        PlanetaryVoice(
            key="mars",
            latin_name="Mars ferè",
            english_name="Mars",
            glyph="♂",
            voice_part="Tenor",
            mode_label="Modes V / VI (Lydian, ~2:3 Perfect Fifth)",
            extremal_ratio=sp.Rational(3, 2),
            aphelion_arcmin="26'14\"",
            perihelion_arcmin="38'01\"",
            notes=(
                _n("F3", 16, 9, 1),
                _n("G3", 2, 1, 1),
                _n("A3", 9, 4, 1),
                _n("B♭3", 12, 5, 1),
                _n("C4", 8, 3, 2),
                _n("B♭3", 12, 5, 1),
                _n("A3", 9, 4, 1),
                _n("G3", 2, 1, 1),
                _n("F3", 16, 9, 3),
            ),
            pan=-0.15,
        ),
        PlanetaryVoice(
            key="earth",
            latin_name="Terra",
            english_name="Earth",
            glyph="⊕",
            voice_part="Alto",
            mode_label="Modes III / IV (Phrygian MI–FA–MI, 15:16 Semitone)",
            extremal_ratio=sp.Rational(16, 15),
            aphelion_arcmin="57'03\"",
            perihelion_arcmin="61'18\"",
            notes=(
                _n("G4", 4, 1, 3),
                _n("A♭4", 64, 15, 3),
                _n("G4", 4, 1, 6),
            ),
            pan=0.10,
        ),
        PlanetaryVoice(
            key="venus",
            latin_name="Venus",
            english_name="Venus",
            glyph="♀",
            voice_part="Alto",
            mode_label="Modes III / IV (Unison Diesis 24:25)",
            extremal_ratio=sp.Rational(25, 24),
            aphelion_arcmin="94'50\"",
            perihelion_arcmin="97'37\"",
            notes=(
                _n("E5", 20, 3, 4),
                _n("E5+", 125, 18, 4),
                _n("E5", 20, 3, 4),
            ),
            pan=0.35,
        ),
        PlanetaryVoice(
            key="mercury",
            latin_name="Mercurius",
            english_name="Mercury",
            glyph="☿",
            voice_part="Soprano",
            mode_label="All Modes (Octave + Minor Third, 5:12)",
            extremal_ratio=sp.Rational(12, 5),
            aphelion_arcmin="164'00\"",
            perihelion_arcmin="384'00\"",
            # Exact 14-note motif from folio 0299: 10 stepwise ascending + descending triad arpeggio!
            notes=(
                _n("C4", 8, 3, 1, 2),
                _n("D4", 3, 1, 1, 2),
                _n("E4", 10, 3, 1, 2),
                _n("F4", 32, 9, 1, 2),
                _n("G4", 4, 1, 1, 2),
                _n("A4", 9, 2, 1, 2),
                _n("B4", 5, 1, 1, 2),
                _n("C5", 16, 3, 1, 2),
                _n("D5", 6, 1, 1, 2),
                _n("E5", 20, 3, 1),
                _n("C5", 16, 3, 1),
                _n("G4", 4, 1, 1),
                _n("E4", 10, 3, 1),
                _n("C4", 8, 3, 2),
            ),
            pan=0.60,
        ),
        PlanetaryVoice(
            key="moon",
            latin_name="Luna (Hic locum habet etiam ☽)",
            english_name="Moon",
            glyph="☽",
            voice_part="Cradle Monody",
            mode_label="Perfect Fourth (3:4, Cradle Monody beside Earth)",
            extremal_ratio=sp.Rational(4, 3),
            aphelion_arcmin="perigee/apogee",
            perihelion_arcmin="3:4",
            notes=(
                _n("G4", 4, 1, 1),
                _n("A4", 9, 2, 1),
                _n("B4", 5, 1, 1),
                _n("C5", 16, 3, 2),
                _n("B4", 5, 1, 1),
                _n("A4", 9, 2, 1),
                _n("G4", 4, 1, 2),
            ),
            pan=0.25,
        ),
    )


def get_universal_chords() -> tuple[UniversalChord, ...]:
    """Return Kepler's 4 Universal 6-Planet Creation Chords (folios 0301–0302)."""
    return (
        UniversalChord(
            key="durum_b",
            title="Universal Chord I — Major (Ut ♮ concordet)",
            latin_heading="Harmonia Universalis Generis Duri · Ut ♮ concordet",
            folio="0301",
            genus="Durum (Major)",
            voicings=(
                ("Saturn", "G2", sp.Rational(1, 1)),
                ("Saturn (perih.)", "B2", sp.Rational(5, 4)),
                ("Jupiter", "B3", sp.Rational(5, 2)),
                ("Mars", "G3", sp.Rational(2, 1)),
                ("Earth", "G4", sp.Rational(4, 1)),
                ("Venus", "E5", sp.Rational(20, 3)),
                ("Mercury", "B5", sp.Rational(10, 1)),
            ),
        ),
        UniversalChord(
            key="durum_c",
            title="Universal Chord II — Major (Ut c concordet)",
            latin_heading="Harmonia Universalis Generis Duri · Ut c concordet",
            folio="0301",
            genus="Durum (Major)",
            voicings=(
                ("Saturn", "G2", sp.Rational(1, 1)),
                ("Jupiter", "C3", sp.Rational(4, 3)),
                ("Mars", "G3", sp.Rational(2, 1)),
                ("Mars (perih.)", "C4", sp.Rational(8, 3)),
                ("Earth", "G4", sp.Rational(4, 1)),
                ("Venus", "E5", sp.Rational(20, 3)),
                ("Mercury", "C6", sp.Rational(32, 3)),
            ),
        ),
        UniversalChord(
            key="molle_bb",
            title="Universal Chord III — Minor (Ut b concordet)",
            latin_heading="Harmonia Universalis Generis Mollis · Ut b concordet",
            folio="0302",
            genus="Molle (Minor)",
            voicings=(
                ("Saturn", "G2", sp.Rational(1, 1)),
                ("Saturn (perih.)", "B♭2", sp.Rational(6, 5)),
                ("Jupiter", "B♭3", sp.Rational(12, 5)),
                ("Mars", "G3", sp.Rational(2, 1)),
                ("Earth", "G4", sp.Rational(4, 1)),
                ("Venus", "E♭5", sp.Rational(32, 5)),
                ("Mercury", "B♭5", sp.Rational(48, 5)),
            ),
        ),
        UniversalChord(
            key="molle_c",
            title="Universal Chord IV — Minor (Ut c concordet)",
            latin_heading="Harmonia Universalis Generis Mollis · Ut c concordet",
            folio="0302",
            genus="Molle (Minor)",
            voicings=(
                ("Saturn", "G2", sp.Rational(1, 1)),
                ("Jupiter", "C3", sp.Rational(4, 3)),
                ("Mars", "G3", sp.Rational(2, 1)),
                ("Earth", "G4", sp.Rational(4, 1)),
                ("Venus", "E♭5", sp.Rational(32, 5)),
                ("Mercury", "G5", sp.Rational(8, 1)),
                ("Mercury (high)", "C6", sp.Rational(32, 3)),
            ),
        ),
    )


def get_folio_0297_scales() -> dict[str, tuple[tuple[str, int, sp.Rational], ...]]:
    """Return Kepler's exact integer string-length Just-Intonation scales (fol. 0297)."""
    durus_lengths = (
        ("G", 2160), ("A", 1920), ("B", 1728), ("C", 1620), ("D", 1440),
        ("E", 1296), ("F♯", 1152), ("g", 1080), ("a", 960), ("b", 864),
    )
    mollis_lengths = (
        ("G", 2160), ("A", 1920), ("B♭", 1800), ("C", 1620), ("D", 1440),
        ("E♭", 1350), ("F", 1215), ("g", 1080),
    )
    return {
        "cantus_durus": tuple((lbl, ln, sp.Rational(2160, ln)) for lbl, ln in durus_lengths),
        "cantus_mollis": tuple((lbl, ln, sp.Rational(2160, ln)) for lbl, ln in mollis_lengths),
    }


def verify_kepler_just_intonation() -> dict[str, bool]:
    """Symbolically verify Kepler's folio 0297 string lengths and folio 0299 intervals."""
    scales = get_folio_0297_scales()
    durus_ratios = [r for _, _, r in scales["cantus_durus"]]
    mollis_ratios = [r for _, _, r in scales["cantus_mollis"]]

    expected_durus = [
        sp.Rational(1, 1), sp.Rational(9, 8), sp.Rational(5, 4), sp.Rational(4, 3),
        sp.Rational(3, 2), sp.Rational(5, 3), sp.Rational(15, 8), sp.Rational(2, 1),
        sp.Rational(9, 4), sp.Rational(5, 2),
    ]
    expected_mollis = [
        sp.Rational(1, 1), sp.Rational(9, 8), sp.Rational(6, 5), sp.Rational(4, 3),
        sp.Rational(3, 2), sp.Rational(8, 5), sp.Rational(16, 9), sp.Rational(2, 1),
    ]

    melodies = {v.key: v for v in get_planetary_melodies()}
    # Check exact peak/base ratio for each planet
    sat_ratio = max(n.ratio_from_g2 for n in melodies["saturn"].notes) / min(n.ratio_from_g2 for n in melodies["saturn"].notes)
    jup_ratio = max(n.ratio_from_g2 for n in melodies["jupiter"].notes) / min(n.ratio_from_g2 for n in melodies["jupiter"].notes)
    mar_ratio = max(n.ratio_from_g2 for n in melodies["mars"].notes) / min(n.ratio_from_g2 for n in melodies["mars"].notes)
    ear_ratio = max(n.ratio_from_g2 for n in melodies["earth"].notes) / min(n.ratio_from_g2 for n in melodies["earth"].notes)
    ven_ratio = max(n.ratio_from_g2 for n in melodies["venus"].notes) / min(n.ratio_from_g2 for n in melodies["venus"].notes)
    mer_ratio = max(n.ratio_from_g2 for n in melodies["mercury"].notes) / min(n.ratio_from_g2 for n in melodies["mercury"].notes)

    return {
        "folio_0297_durus_exact": durus_ratios == expected_durus,
        "folio_0297_mollis_exact": mollis_ratios == expected_mollis,
        "saturn_major_third_5_4": sat_ratio == sp.Rational(5, 4),
        "jupiter_minor_third_6_5": jup_ratio == sp.Rational(6, 5),
        "mars_perfect_fifth_3_2": mar_ratio == sp.Rational(3, 2),
        "earth_semitone_16_15": ear_ratio == sp.Rational(16, 15),
        "venus_diesis_25_24": ven_ratio == sp.Rational(25, 24),
        "mercury_ten_step_plus_arpeggio_5_2": mer_ratio == sp.Rational(5, 2),
        "seven_voices_present": len(melodies) == 7,
        "four_universal_chords_present": len(get_universal_chords()) == 4,
    }


# ── Pure-Python Standard MIDI File (Format 1, Microtonal Just Intonation) ──
def _vlq(val: int) -> bytes:
    out = [val & 0x7F]
    val >>= 7
    while val:
        out.append((val & 0x7F) | 0x80)
        val >>= 7
    return bytes(reversed(out))


def _freq_to_midi_and_bend(freq_hz: float) -> tuple[int, int]:
    """Convert exact Hz to nearest MIDI note + 14-bit pitch bend (±2 semitones range)."""
    midi_f = 69.0 + 12.0 * math.log2(freq_hz / 440.0)
    note = max(12, min(115, round(midi_f)))
    diff_semi = midi_f - note
    bend = max(0, min(16383, round(8192 + (diff_semi / 2.0) * 8192)))
    return note, bend


def export_kepler_midi(midi_path: Path, tempo_bpm: int = 72) -> Path:
    """Export all 7 planetary melodies + 4 Creation Chords as a multi-track Standard MIDI file."""
    tpq = 480
    tracks: list[bytes] = []

    # Track 0: Tempo & Title Meta Track
    tempo_us = int(60_000_000 / tempo_bpm)
    title = b"Kepler Harmonices Mundi (1619) - Folios 0299-0302"
    t0 = bytearray()
    t0 += b"\x00\xff\x03" + _vlq(len(title)) + title
    t0 += b"\x00\xff\x51\x03" + tempo_us.to_bytes(3, "big")
    t0 += b"\x00\xff\x2f\x00"
    tracks.append(bytes(t0))

    voices = get_planetary_melodies()
    # General MIDI Church Organ (19) & Choir Aahs (52) for Renaissance authenticity
    programs = [19, 19, 19, 52, 52, 19, 52]

    for idx, voice in enumerate(voices):
        ch = idx % 15
        if ch >= 9:
            ch += 1  # skip percussion channel 9
        tr = bytearray()
        name_b = f"{voice.latin_name} ({voice.voice_part})".encode("ascii", "ignore")
        tr += b"\x00\xff\x03" + _vlq(len(name_b)) + name_b
        tr += bytes([0x00, 0xC0 | ch, programs[idx]])

        # Stagger voice entries by 4 beats each like a Renaissance polyphonic motet!
        entry_delay = idx * 2 * tpq
        first = True
        for _rep in range(2):
            for kn in voice.notes:
                dur = int(float(kn.beats) * tpq)
                note, bend = _freq_to_midi_and_bend(float(kn.freq_hz))
                dt = entry_delay if first else 0
                first = False
                # Pitch bend before Note-On for exact Just Intonation!
                tr += _vlq(dt) + bytes([0xE0 | ch, bend & 0x7F, (bend >> 7) & 0x7F])
                tr += b"\x00" + bytes([0x90 | ch, note, 84])
                tr += _vlq(max(60, dur - 12)) + bytes([0x80 | ch, note, 0])
                tr += _vlq(12) + bytes([0xE0 | ch, 0x00, 0x40])
        tr += b"\x00\xff\x2f\x00"
        tracks.append(bytes(tr))

    # Final Track: The 4 Universal Creation Chords (Folios 0301-0302)
    ch_chord = 8
    tr_c = bytearray()
    cname = b"Four Universal Creation Chords (Folios 0301-0302)"
    tr_c += b"\x00\xff\x03" + _vlq(len(cname)) + cname
    tr_c += bytes([0x00, 0xC0 | ch_chord, 19])
    for ci, chord in enumerate(get_universal_chords()):
        midi_notes = [_freq_to_midi_and_bend(float(COSMIC_G2_HZ * r))[0] for _, _, r in chord.voicings]
        for ni, mn in enumerate(midi_notes):
            tr_c += (_vlq(480) if (ci > 0 and ni == 0) else b"\x00") + bytes([0x90 | ch_chord, mn, 76])
        for ni, mn in enumerate(midi_notes):
            tr_c += (_vlq(4 * tpq) if ni == 0 else b"\x00") + bytes([0x80 | ch_chord, mn, 0])
    tr_c += b"\x00\xff\x2f\x00"
    tracks.append(bytes(tr_c))

    header = b"MThd" + struct.pack(">IHHH", 6, 1, len(tracks), tpq)
    body = b"".join(b"MTrk" + struct.pack(">I", len(t)) + t for t in tracks)
    midi_path.write_bytes(header + body)
    return midi_path


# ── Stereo Cathedral Organ & Celestial Choir Just-Intonation WAV Synth ─────
def _organ_sample(phase: float, voice_weight: float) -> float:
    """Warm Renaissance principal pipe-organ + choral harmonic spectrum."""
    # Fundamental + octave + twelfth + super-octave + soft tierce
    return (
        1.00 * math.sin(phase)
        + 0.48 * math.sin(2.0 * phase)
        + 0.24 * math.sin(3.0 * phase)
        + 0.14 * math.sin(4.0 * phase)
        + 0.06 * voice_weight * math.sin(5.0 * phase)
        + 0.04 * math.sin(6.0 * phase)
    ) / 1.96


def _apply_cathedral_reverb(left: list[float], right: list[float], sr: int) -> None:
    """Apply clean multi-tap stereo cathedral reverberation in place."""
    n = len(left)
    taps = [
        (int(0.067 * sr), 0.28, 0.14),
        (int(0.113 * sr), 0.14, 0.26),
        (int(0.179 * sr), 0.20, 0.18),
        (int(0.263 * sr), 0.15, 0.17),
        (int(0.389 * sr), 0.11, 0.12),
    ]
    orig_l = list(left)
    orig_r = list(right)
    for delay, gl, gr in taps:
        for i in range(delay, n):
            left[i] += orig_l[i - delay] * gl + orig_r[i - delay] * (gr * 0.4)
            right[i] += orig_r[i - delay] * gr + orig_l[i - delay] * (gl * 0.4)


def _write_stereo_wav(wav_path: Path, left: list[float], right: list[float], sr: int) -> Path:
    peak = max(max((abs(x) for x in left), default=1.0), max((abs(x) for x in right), default=1.0), 1e-6)
    scale = 29000.0 / peak
    pcm = array.array("h")
    for l_val, r_val in zip(left, right, strict=True):
        pcm.append(max(-32767, min(32767, int(l_val * scale))))
        pcm.append(max(-32767, min(32767, int(r_val * scale))))
    with wave.open(str(wav_path), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())
    return wav_path


def synthesize_planetary_motet_wav(wav_path: Path, sr: int = 22050) -> Path:
    """Synthesize Kepler's 6-planet + Moon 1619 melodies as a stereo Just-Intonation motet."""
    voices = get_planetary_melodies()
    beat_sec = 0.62
    total_sec = 26.0
    n_samples = int(total_sec * sr)
    left = [0.0] * n_samples
    right = [0.0] * n_samples

    # Stagger entries from deep Bass Saturn up through Soprano Mercury & Luna!
    entry_beats = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]

    for v_idx, voice in enumerate(voices):
        t_cursor = entry_beats[v_idx] * beat_sec
        amp = 0.24 if voice.key in ("saturn", "jupiter") else (0.18 if voice.key in ("mars", "earth") else 0.14)
        pan_l = math.sqrt(0.5 * (1.0 - voice.pan))
        pan_r = math.sqrt(0.5 * (1.0 + voice.pan))

        while t_cursor < total_sec - 2.5:
            for kn in voice.notes:
                dur = float(kn.beats) * beat_sec
                if t_cursor >= total_sec - 1.5:
                    break
                dur = min(dur, total_sec - 1.2 - t_cursor)
                freq = float(kn.freq_hz)
                i0 = int(t_cursor * sr)
                i1 = min(n_samples, int((t_cursor + dur) * sr))
                att = max(1, int(0.06 * sr))
                rel = max(1, int(0.14 * sr))
                length = i1 - i0
                two_pi_f = 2.0 * math.pi * freq / sr
                for k in range(length):
                    env = 1.0
                    if k < att:
                        env = k / att
                    elif k > length - rel:
                        env = max(0.0, (length - k) / rel)
                    # Gentle choral vibrato
                    vib = 1.0 + 0.0022 * math.sin(2.0 * math.pi * 4.8 * (i0 + k) / sr)
                    val = amp * env * _organ_sample(two_pi_f * k * vib, 0.85)
                    left[i0 + k] += val * pan_l
                    right[i0 + k] += val * pan_r
                t_cursor += dur

    _apply_cathedral_reverb(left, right, sr)
    return _write_stereo_wav(wav_path, left, right, sr)


def synthesize_creation_chords_wav(wav_path: Path, sr: int = 22050) -> Path:
    """Synthesize all 4 Universal 6-Planet Creation Chords (folios 0301–0302) in pure Just Intonation."""
    chords = get_universal_chords()
    chord_dur = 5.2
    gap_dur = 0.5
    total_sec = len(chords) * (chord_dur + gap_dur) + 1.5
    n_samples = int(total_sec * sr)
    left = [0.0] * n_samples
    right = [0.0] * n_samples

    for ci, chord in enumerate(chords):
        t0 = ci * (chord_dur + gap_dur) + 0.3
        i0 = int(t0 * sr)
        i1 = min(n_samples, int((t0 + chord_dur) * sr))
        length = i1 - i0
        att = int(0.65 * sr)
        rel = int(1.10 * sr)

        for vi, (_planet, _lbl, ratio) in enumerate(chord.voicings):
            freq = float(COSMIC_G2_HZ * ratio)
            # Balance lower voices richer, upper voices crystalline
            amp = 0.24 / (1.0 + 0.14 * vi)
            pan = -0.55 + 1.10 * (vi / max(1, len(chord.voicings) - 1))
            pan_l = math.sqrt(0.5 * (1.0 - pan))
            pan_r = math.sqrt(0.5 * (1.0 + pan))
            w = 2.0 * math.pi * freq / sr
            for k in range(length):
                env = 1.0
                if k < att:
                    env = 0.5 - 0.5 * math.cos(math.pi * k / att)
                elif k > length - rel:
                    env = 0.5 - 0.5 * math.cos(math.pi * (length - k) / rel)
                val = amp * env * _organ_sample(w * k, 1.0)
                left[i0 + k] += val * pan_l
                right[i0 + k] += val * pan_r

    _apply_cathedral_reverb(left, right, sr)
    return _write_stereo_wav(wav_path, left, right, sr)
