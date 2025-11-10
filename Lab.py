Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... 
...  def spp_ls(sat_ecef, pseudorange, x0, weights=None, max_iter=8, tol=1e-4):
...  
...  x = np.array(x0, dtype=float)
...  for _ in range(max_iter):
...  H, v = [], []
...  for s, rho in zip(sat_ecef, pseudorange):
...  r = np.linalg.norm(x[:3]- s)
...  los = (x[:3]- s) / r
...  rho_hat = r + x[3]
...  v.append(rho- rho_hat)
...  H.append(np.r_[los, 1.0])
...  H = np.array(H); v = np.array(v)
...  W = np.diag(weights) if weights is not None else np.eye(len(v))
...  dx = np.linalg.solve(H.T @ W @ H, H.T @ W @ v)
...  x += dx
...  if np.linalg.norm(dx) < tol: break
