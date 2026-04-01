# FCC `X` Point in Quantum ESPRESSO

This note summarizes why the `X` point for an FCC lattice appears in Quantum ESPRESSO as

```text
1.0 0.0 0.0
```

when the q-vector is given in units of `2pi/alat`.

## 1. Real-space primitive lattice

Start from the FCC primitive lattice vectors

\[
\mathbf{v}_1 = \frac{a}{2}(-1,0,1), \quad
\mathbf{v}_2 = \frac{a}{2}(0,1,1), \quad
\mathbf{v}_3 = \frac{a}{2}(-1,1,0).
\]

These are written with respect to a fixed Cartesian `x,y,z` axis system.

The primitive-cell volume is

\[
\Omega = \mathbf{v}_1 \cdot (\mathbf{v}_2 \times \mathbf{v}_3) = \frac{a^3}{4}.
\]

## 2. Reciprocal lattice

The reciprocal vectors are defined by

\[
\mathbf{b}_1 = 2\pi \frac{\mathbf{v}_2 \times \mathbf{v}_3}{\Omega}, \quad
\mathbf{b}_2 = 2\pi \frac{\mathbf{v}_3 \times \mathbf{v}_1}{\Omega}, \quad
\mathbf{b}_3 = 2\pi \frac{\mathbf{v}_1 \times \mathbf{v}_2}{\Omega}.
\]

Carrying out the cross products gives

\[
\mathbf{b}_1 = \frac{2\pi}{a}(-1,-1,1),
\]

\[
\mathbf{b}_2 = \frac{2\pi}{a}(1,1,1),
\]

\[
\mathbf{b}_3 = \frac{2\pi}{a}(-1,1,-1).
\]

So the reciprocal lattice of FCC is BCC.

## 3. Why `X` lies at the Brillouin-zone boundary

To find the point labeled `X`, move from `Gamma` along the Cartesian `[100]` direction:

\[
\mathbf{q} = \xi \frac{2\pi}{a}(1,0,0).
\]

The Brillouin-zone boundary is reached when `q` is equally distant from `Gamma` and from a reciprocal-lattice point `G`:

\[
|\mathbf{q}|^2 = |\mathbf{q} - \mathbf{G}|^2.
\]

Along `[100]`, the relevant reciprocal-lattice vector is

\[
\mathbf{G} = \frac{2\pi}{a}(2,0,0).
\]

This is a valid reciprocal-lattice vector because

\[
\mathbf{G} = -\mathbf{b}_1 - \mathbf{b}_3.
\]

Apply the boundary condition:

\[
\mathbf{q} \cdot \mathbf{G} = \frac{|\mathbf{G}|^2}{2}.
\]

Substitute `q` and `G`:

\[
\left( \xi \frac{2\pi}{a}(1,0,0) \right)
\cdot
\left( \frac{2\pi}{a}(2,0,0) \right)
=
\frac{1}{2}
\left| \frac{2\pi}{a}(2,0,0) \right|^2.
\]

This gives

\[
2\xi \left( \frac{2\pi}{a} \right)^2
=
2 \left( \frac{2\pi}{a} \right)^2,
\]

so

\[
\xi = 1.
\]

Therefore,

\[
\mathbf{X} = \frac{2\pi}{a}(1,0,0).
\]

This means `X` is a Brillouin-zone boundary point. More specifically, for FCC it is the center of a square face of the Brillouin zone.

## 4. Why QE writes it as `1.0 0.0 0.0`

In `ph.x`, the q-vector is given in Cartesian units of `2pi/alat`, where `alat` is the lattice parameter used by QE.

So the vector

\[
\mathbf{X} = \frac{2\pi}{a}(1,0,0)
\]

is entered simply as

```text
1.0 0.0 0.0
```

This is a Cartesian representation, not a coordinate along the reciprocal primitive basis vectors `b1, b2, b3`.

## 5. The same `X` point in the reciprocal primitive basis

The same physical point can also be written as a combination of `b1, b2, b3`:

\[
\mathbf{X} = -\frac{1}{2}\mathbf{b}_1 - \frac{1}{2}\mathbf{b}_3.
\]

So:

- in Cartesian coordinates, `X` is along `[100]`
- in reciprocal-basis coordinates, `X` is a linear combination of `b1, b2, b3`

These are two descriptions of the same point.

## 6. Notes for the Si diamond structure

For Si in QE, one often uses:

- `ibrav = 2` for FCC
- `nat = 2` for the two-atom diamond basis
- `ntyp = 1` because both atoms are Si

The two-atom basis changes the phonon branches, but it does not change the Brillouin-zone geometry. The location of `X` is determined by the Bravais lattice, not by the basis.

## 7. Common points of confusion

### `X` is a vector, not a scalar

It is better to say

\[
\mathbf{X} = \frac{2\pi}{a}(1,0,0)
\]

than to say only "`X` is `2pi/a`", because `X` is a point in reciprocal space with direction and magnitude.

### QE uses Cartesian `2pi/alat` units here

The input

```text
1.0 0.0 0.0
```

does not mean "`1` along `b1`". It means a vector along the Cartesian `x` direction with magnitude `2pi/a`.

### `X` is along `[100]`, not along `b1`

For this FCC primitive cell,

\[
\mathbf{b}_1 = \frac{2\pi}{a}(-1,-1,1),
\]

which is not along Cartesian `[100]`.

### Different books may give different coordinates for the same `X`

This usually happens because one source uses Cartesian coordinates while another uses coordinates in the reciprocal primitive basis. The coordinates look different, but the point is the same.

### `nat = 2` does not move the high-symmetry points

The basis changes the dynamical matrix and the number of phonon branches, but the Brillouin zone itself is still the one for the FCC Bravais lattice.

## 8. Short conclusion

For the FCC primitive lattice,

\[
\mathbf{X} = \frac{2\pi}{a}(1,0,0)
\]

is the first Brillouin-zone boundary point reached along Cartesian `[100]`. That is why Quantum ESPRESSO uses

```text
1.0 0.0 0.0
```

for the `X`-point phonon calculation.
