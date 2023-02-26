# Material-Heterogoneity
modeling material heterogeneity with size effects using spatially-correlated weibull distribution
the python script generates a grid of random values from weibul distribution using inverse transform method. m is the heterogeneity index. Larger values of $m$ results in less variation, and as it approaches infinity, the material becomes homogeneous. The spatial correlation length factor $\theta$ describes the correlation degree between elements. A smaller correlation factor means larger gradient of values, which can be used to include size effects.
$theta=0.1:$
![theta=0 1](https://user-images.githubusercontent.com/69943289/221440559-9cf780e6-c335-4bf3-976c-aca2fcbd8fd8.jpg)
$theta=0.5:$
![theta=0 5](https://user-images.githubusercontent.com/69943289/221440574-784e27b7-f808-4a8c-a7cf-36122d6ff234.jpg)
$theta=2.0:$
![theta=2 0](https://user-images.githubusercontent.com/69943289/221440589-afc89886-be2f-46b8-b242-858e4c34233c.jpg)
$theta=5.0:$
![theta=5 0](https://user-images.githubusercontent.com/69943289/221440596-e1184223-5d3d-444f-bd92-3c179a1fcec5.jpg)
