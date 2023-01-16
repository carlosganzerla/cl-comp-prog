(defun check (s)
  (do ((i 0 (1+ i)))
      ((>= i (length s)) t)
      (unless (char= (char s (mod (1+ i) (length s)))
                     (char s (mod (1- i) (length s))))
        (return nil))))


(defun main ()
  (dotimes (_ (read))
    (if (check (read-line))
        (write-string "YES")
        (write-string "NO"))
    (terpri)))

(main)
