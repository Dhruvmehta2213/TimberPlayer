# Scenarios to check against TimberMusicPlayer model used as oracle

from TimberMusicPlayer import InitializePlayer, PlayMusic, PauseMusic

testSuite = [
  # Run 1
  [
     (PlayMusic, (), None),
     (PauseMusic, (), None),
     (PlayMusic, (), None)
  ],
  # Run 2
  [
      (PlayMusic, (), None),
      (PauseMusic, (), None),
      (PlayMusic, (), None),
      (InitializePlayer,(),None)
  ],
  # Run 3
  [
     (PlayMusic, (), None),
     (PauseMusic, (), None),
     (InitializePlayer,(),None)
  ],
  # Run 4
  [
     (PauseMusic, (), None),
     (PlayMusic, (), None),
     (PauseMusic, (), None),
     (InitializePlayer,(),None),
     (PlayMusic, (), None)
  ]
]
