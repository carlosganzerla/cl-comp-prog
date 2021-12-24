(defun read-multiple ()
  (values-list (read-from-string (concatenate 'string "(" (read-line) ")"))))

(defun read-integers ()
  (multiple-value-bind (n k) (read-multiple)
    (do ((x 1 (1+ x))
        (total 0))
        ((> x n) total)
        (when (= 0 (mod (read) k))
          (incf total)))))

(defun main ()
  (princ (read-integers)))
