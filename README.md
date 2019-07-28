# 1D Vision
> a study on ray casting for the one or two eyed classical flatlander

An exploration of the theoretical vision apparatus of a creature living on a 2D plane. 
Just as us humans percieve the wold with reduced dimensionality (3D world, 2D image), the flatlander's eyes percieve 
the world in only a single dimension. 

### -- Work in progress --

The idea of this project is to implement binocular vision for the two eyed creature via ray casting algorithms. And that way - analogous to human vision - recover depth information about its envoironment. Therefore, the correspondence problem needs to be solved [https://en.wikipedia.org/wiki/Correspondence_problem]

## Prerequisites

To run main.py, pygame and numpy need to be installed.

```
$ pip install pygame
$ pip install numpy 
```

## Creatures

Binocular Creature         |  Cyclops (known ray length)
:-------------------------:|:-------------------------:
![](https://...Dark.png)  |  ![](https://...Ocean.png)

The program currently supports two creatures. 
- The standard Creature has two eyes that each generate a 1D image.
- The Cyclops has only one eye but - for demonstration purposes - is given the lengths of the rays to allow for 2D vision.

One can easily switch between characters in main.py

```python
char = Creature(Position(200,200), window)
char = Cyclops(Position(200,200), window)
```

## Meta

Philipp Skudlik 

[https://github.com/pskugit](https://github.com/pskugit/)

