import numpy as np
import matplotlib.pyplot as plt

c = 1.0
k = np.linspace(-np.pi, np.pi, 2000)

one_minus_e = 1.0 - np.exp(-1j * k)

mass_cases = [
    (3.0, "1.png", "Heavy-Mass Regime ($mc^2 = 3 > 2c$)"),
    (2.0, "2.png", "Critical Regime ($mc^2 = 2 = 2c$)"),
    (1.0, "3.png", "Light-Mass Regime ($mc^2 = 1 < 2c$)"),
]

for m, filename, title in mass_cases:

  term = m**2 * c**4 - c**2 * (one_minus_e**2)
  lam_plus = np.sqrt(term)
  lam_minus = -lam_plus

  plt.figure(figsize=(4, 4))
  plt.plot(
      np.real(lam_plus),
      np.imag(lam_plus),
      "b-",
      linewidth=2,
      label=r"$\lambda_+(k)$",
  )
  plt.plot(
      np.real(lam_minus),
      np.imag(lam_minus),
      "r--",
      linewidth=2,
      label=r"$\lambda_-(k)$",
  )

  plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
  plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
  plt.title(
      f"Spectrum $\\sigma(D_d)$ for $c = {c}$, $m = {m}$\n{title}", fontsize=11
  )
  plt.xlabel(r"$\operatorname{Re} \lambda$", fontsize=10)
  plt.ylabel(r"$\operatorname{Im} \lambda$", fontsize=10)
  plt.grid(True, linestyle=":", alpha=0.6)
  plt.legend(loc="upper right")
  plt.axis("equal")

  plt.tight_layout()
  plt.savefig(filename, dpi=300)
  plt.close()

print("Plots 1.png, 2.png, and 3.png generated successfully.")
