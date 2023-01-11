(defun max-iterations (tmax nmax sum)
  (do ((i 0 (1+ i))
       (remaining sum)
       (iterations 0))
      ((or (>= 0 remaining) (>= i tmax)) iterations)
      (let ((debit (min remaining nmax)))
        (decf remaining debit)
        (incf iterations (expt debit 2)))))


(defun main ()
  (dotimes (_ (read))
    (format t "~A~%" (max-iterations (read) (read) (read)))))

(main)
