(defun fac (n)
  (labels ((rec (n acc)
             (if (> n 1)
                 (rec (1- n) (* n acc))
                 acc)))
    (rec n 1)))

(print (fac (read)))
