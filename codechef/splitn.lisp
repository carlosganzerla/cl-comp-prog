(defun ops (X &optional (i 0))
  (let* ((d (log X 2))
         (dtrunc (truncate d)))
    (if (= d dtrunc)
        i
        (ops (- X (expt 2 dtrunc)) (1+ i)))))

(defun main ()
  (dotimes (_ (read))
    (print (ops (read)))))

(main)
